/**
 * Backend API Integration
 * Handles pipeline and analytics execution via backend API or direct execution
 */

const API_BASE_URL = '/api'; // Change to actual backend URL if needed
const PROJECT_ROOT = '..'; // Relative path to project root from ui/

/**
 * Execute ETL pipeline
 */
async function runPipeline() {
  const button = document.querySelector('#run-etl-btn');
  const status = document.querySelector('#etl-status');
  
  if (!button || !status) return;
  
  // Disable button and show loading state
  button.disabled = true;
  const buttonText = button.querySelector('span') || button;
  const originalText = buttonText.textContent;
  buttonText.textContent = 'RUNNING...';
  status.className = 'status info';
  status.textContent = 'RUNNING... Please wait.';
  
  try {
    // Try backend API first
    const response = await fetch(`${API_BASE_URL}/pipeline/run`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }
    });
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data = await response.json();
    
    if (data.status === 'success') {
      status.className = 'status success';
      status.textContent = `✅ Pipeline complete! Events: ${data.metrics.events_count?.toLocaleString() || 'N/A'}, Sessions: ${data.metrics.session_count?.toLocaleString() || 'N/A'}, View→Cart: ${data.metrics.view_to_cart_rate?.toFixed(2) || 'N/A'}%, Cart→Purchase: ${data.metrics.cart_to_purchase_rate?.toFixed(2) || 'N/A'}%`;
      updatePipelineSummary(data.metrics);
    } else {
      status.className = 'status error';
      status.textContent = `❌ Error: ${data.message || 'Unknown error'}`;
    }
  } catch (error) {
    // Fallback: Show helpful error message
    status.className = 'status error';
    status.textContent = `❌ Error: ${error.message}. Ensure backend server is running (see README) or run manually: python src/etl_funnel.py`;
    console.error('Pipeline execution error:', error);
  } finally {
    button.disabled = false;
    buttonText.textContent = originalText;
  }
}

/**
 * Execute analytics queries
 */
async function runAnalytics() {
  const button = document.querySelector('#run-analytics-btn');
  const status = document.querySelector('#analytics-status');
  
  if (!button || !status) return;
  
  // Disable button and show loading state
  button.disabled = true;
  const buttonText = button.querySelector('span') || button;
  const originalText = buttonText.textContent;
  buttonText.textContent = 'RUNNING...';
  status.className = 'status info';
  status.textContent = 'RUNNING... Please wait.';
  
  try {
    // Try backend API first
    const response = await fetch(`${API_BASE_URL}/analytics/run`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }
    });
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data = await response.json();
    
    if (data.status === 'success') {
      status.className = 'status success';
      status.textContent = `✅ Analytics complete! Exported ${data.exports?.[0]?.rows || 0} rows to sku_dropoff.csv, ${data.exports?.[1]?.rows || 0} rows to cohort_retention.csv`;
      updateAnalyticsExports(data.exports);
    } else {
      status.className = 'status error';
      status.textContent = `❌ Error: ${data.message || 'Unknown error'}`;
    }
  } catch (error) {
    // Fallback: Show helpful error message
    status.className = 'status error';
    status.textContent = `❌ Error: ${error.message}. Ensure backend server is running (see README) or run manually: python src/run_analytics.py`;
    console.error('Analytics execution error:', error);
  } finally {
    button.disabled = false;
    buttonText.textContent = originalText;
  }
}

/**
 * Get artifact list and row counts
 */
async function getArtifacts() {
  try {
    const response = await fetch(`${API_BASE_URL}/artifacts`);
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data = await response.json();
    return data.files || [];
  } catch (error) {
    console.error('Artifact fetch error:', error);
    // Return empty array on error
    return [];
  }
}

/**
 * Update pipeline summary section
 */
function updatePipelineSummary(metrics) {
  const summary = document.querySelector('#pipeline-summary');
  if (!summary || !metrics) return;
  
  const eventsEl = summary.querySelector('[data-metric="events"]');
  const stepsEl = summary.querySelector('[data-metric="steps"]');
  const sessionsEl = summary.querySelector('[data-metric="sessions"]');
  const viewToCartEl = summary.querySelector('[data-metric="view-to-cart"]');
  const cartToPurchaseEl = summary.querySelector('[data-metric="cart-to-purchase"]');
  
  if (eventsEl) eventsEl.textContent = metrics.events_count?.toLocaleString() || '—';
  if (stepsEl) stepsEl.textContent = metrics.steps_count?.toLocaleString() || '—';
  if (sessionsEl) sessionsEl.textContent = metrics.session_count?.toLocaleString() || '—';
  if (viewToCartEl) viewToCartEl.textContent = metrics.view_to_cart_rate ? `${metrics.view_to_cart_rate.toFixed(2)}%` : '—';
  if (cartToPurchaseEl) cartToPurchaseEl.textContent = metrics.cart_to_purchase_rate ? `${metrics.cart_to_purchase_rate.toFixed(2)}%` : '—';
}

/**
 * Update analytics exports section
 */
function updateAnalyticsExports(exports) {
  const skuEl = document.querySelector('[data-export="sku_dropoff"]');
  const cohortEl = document.querySelector('[data-export="cohort_retention"]');
  
  if (skuEl && exports?.[0]) {
    skuEl.textContent = `sku_dropoff.csv — rows: ${exports[0].rows?.toLocaleString() || 'N/A'}`;
  }
  if (cohortEl && exports?.[1]) {
    cohortEl.textContent = `cohort_retention.csv — rows: ${exports[1].rows?.toLocaleString() || 'N/A'}`;
  }
}

/**
 * Update artifact list with row counts
 */
async function updateArtifactList() {
  const artifacts = await getArtifacts();
  const artifactsList = document.querySelector('#artifacts-list');
  const emptyState = document.querySelector('#artifacts-empty');
  
  // Check if any artifacts exist
  const hasArtifacts = artifacts.some(f => f.exists);
  
  if (hasArtifacts) {
    if (artifactsList) artifactsList.style.display = 'grid';
    if (emptyState) emptyState.style.display = 'none';
    
    artifacts.forEach(file => {
      const row = document.querySelector(`[data-artifact="${file.name}"]`);
      if (row) {
        const countEl = row.querySelector('[data-count]');
        if (countEl) {
          if (file.exists && file.rows !== undefined) {
            countEl.textContent = `rows: ${file.rows.toLocaleString()}`;
          } else {
            countEl.textContent = '';
          }
        }
      }
    });
  } else {
    // Show empty state if no artifacts
    if (artifactsList) artifactsList.style.display = 'none';
    if (emptyState) emptyState.style.display = 'block';
  }
}

/**
 * Initialize page-specific functionality
 */
function initPage() {
  const pathname = window.location.pathname;
  const page = pathname.split('/').pop() || 'index.html';
  
  // Pipeline page
  if (page === 'pipeline.html') {
    const button = document.querySelector('#run-etl-btn');
    if (button) {
      button.addEventListener('click', runPipeline);
    }
    
    // Try to load summary if available
    loadPipelineSummary();
  }
  
  // Analytics page
  if (page === 'analytics.html') {
    const button = document.querySelector('#run-analytics-btn');
    if (button) {
      button.addEventListener('click', runAnalytics);
    }
    
    // Try to load exports if available
    loadAnalyticsExports();
  }
  
  // Artifacts page
  if (page === 'artifacts.html') {
    updateArtifactList();
    // Refresh every 30 seconds
    setInterval(updateArtifactList, 30000);
  }
}

/**
 * Load pipeline summary from artifacts (if available)
 */
async function loadPipelineSummary() {
  try {
    const response = await fetch(`${API_BASE_URL}/pipeline/summary`);
    if (response.ok) {
      const data = await response.json();
      if (data.metrics) {
        updatePipelineSummary(data.metrics);
      }
    }
  } catch (error) {
    // Silent fail - summary just won't update
    console.debug('Could not load pipeline summary:', error);
  }
}

/**
 * Load analytics exports info (if available)
 */
async function loadAnalyticsExports() {
  const artifacts = await getArtifacts();
  const skuFile = artifacts.find(f => f.name === 'sku_dropoff.csv');
  const cohortFile = artifacts.find(f => f.name === 'cohort_retention.csv');
  
  if (skuFile) {
    const skuEl = document.querySelector('[data-export="sku_dropoff"]');
    if (skuEl) {
      skuEl.textContent = `sku_dropoff.csv — rows: ${skuFile.exists && skuFile.rows ? skuFile.rows.toLocaleString() : '—'}`;
    }
  }
  
  if (cohortFile) {
    const cohortEl = document.querySelector('[data-export="cohort_retention"]');
    if (cohortEl) {
      cohortEl.textContent = `cohort_retention.csv — rows: ${cohortFile.exists && cohortFile.rows ? cohortFile.rows.toLocaleString() : '—'}`;
    }
  }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPage);
} else {
  initPage();
}

