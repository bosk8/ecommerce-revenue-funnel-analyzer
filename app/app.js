// Navigation: Mark active link based on current page
(function() {
  const pathname = window.location.pathname;
  const currentPage = pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    // Normalize href - remove ./ prefix if present
    const normalizedHref = href.replace(/^\.\//, '');
    // Match if href matches current page filename, or if we're on root and href is index.html
    if (normalizedHref === currentPage || 
        (currentPage === '' && normalizedHref === 'index.html') ||
        (pathname.endsWith('/') && normalizedHref === 'index.html') ||
        (pathname.endsWith('/ui/') && normalizedHref === 'index.html')) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
})();

// Copy to clipboard functionality
(function() {
  const copyButtons = document.querySelectorAll('.copy-btn[data-copy]');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', async function() {
      const textToCopy = this.getAttribute('data-copy');
      const icon = this.querySelector('.copy-icon');
      const checkIcon = this.querySelector('.check-icon');
      
      try {
        await navigator.clipboard.writeText(textToCopy);
        
        // Visual feedback
        if (icon) icon.style.display = 'none';
        if (!checkIcon) {
          const check = document.createElement('span');
          check.className = 'check-icon';
          check.textContent = '✓';
          check.style.display = 'inline';
          this.appendChild(check);
        } else {
          checkIcon.style.display = 'inline';
        }
        
        // Reset after 2 seconds
        setTimeout(() => {
          if (icon) icon.style.display = 'inline';
          if (checkIcon) checkIcon.style.display = 'none';
        }, 2000);
        
        // Announce to screen readers
        const announcement = document.createElement('div');
        announcement.className = 'sr-only';
        announcement.setAttribute('role', 'status');
        announcement.setAttribute('aria-live', 'polite');
        announcement.textContent = 'Copied to clipboard';
        document.body.appendChild(announcement);
        setTimeout(() => announcement.remove(), 2000);
        
      } catch (err) {
        console.error('Failed to copy:', err);
        alert('Failed to copy to clipboard. Please copy manually: ' + textToCopy);
      }
    });
  });
})();

// Screen reader only class
if (!document.querySelector('style[data-sr-only]')) {
  const style = document.createElement('style');
  style.setAttribute('data-sr-only', '');
  style.textContent = '.sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0; }';
  document.head.appendChild(style);
}
