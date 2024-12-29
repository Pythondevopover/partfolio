(function() {
    const snowContainer = document.getElementById('snow');
    for (let i = 0; i < 100; i++) {
      const snowflake = document.createElement('div');
      snowflake.className = 'snowflake';
      snowflake.textContent = '❄';
      snowflake.style.left = Math.random() * 100 + 'vw';
      snowflake.style.animationDuration = Math.random() * 12 + 10 + 's'; // 7-15 soniya oralig'ida
      snowflake.style.fontSize = Math.random() * 10 + 10 + 'px';
      snowContainer.appendChild(snowflake);
    }
  })();
  