const btn = document.getElementById('menuToggle');
    const barraLateral = document.getElementById('barraLateral');

    const setOpen = (open) => {
      barraLateral.classList.toggle('open', open);
      btn.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    };

    btn.addEventListener('click', () => {
      setOpen(!barraLateral.classList.contains('open'));
    });

    // Fecha o menu se clicar fora (em mobile)
    document.addEventListener('click', (e) => {
      const isMobile = window.matchMedia('(max-width: 900px)').matches;
      if (!isMobile) return;
      const clickedOutside = !barraLateral.contains(e.target) && !btn.contains(e.target);
      if (clickedOutside) setOpen(false);
    });

    document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.querySelector(".submenu-toggle");
    const submenu = document.querySelector(".submenu");
      
    toggle.addEventListener("click", () => {
      submenu.classList.toggle("active");
      // Muda a setinha ▾ para ▴
      toggle.innerHTML = toggle.innerHTML.includes("▾")
        ? toggle.innerHTML.replace("▾", "▴")
        : toggle.innerHTML.replace("▴", "▾");
    });
  });
