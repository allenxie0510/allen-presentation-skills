(() => {
  const stage = document.querySelector('.deck-stage');
  const slides = [...document.querySelectorAll('.slide')];
  const counter = document.querySelector('[data-deck-counter]');
  const progress = document.querySelector('[data-deck-progress]');
  const notes = document.querySelector('.notes-panel');
  const deckId = stage?.dataset.deckId || 'presentation';
  let index = Math.max(0, slides.findIndex((slide) => slide.classList.contains('active')));
  let touchStartX = null;

  function scaleStage() {
    if (!stage) return;
    const scale = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
    stage.style.transform = `scale(${scale})`;
    stage.style.left = `${Math.max(0, (window.innerWidth - 1920 * scale) / 2)}px`;
    stage.style.top = `${Math.max(0, (window.innerHeight - 1080 * scale) / 2)}px`;
  }

  function updateNotes() {
    if (!notes || !slides[index]) return;
    notes.textContent = slides[index].dataset.notes || 'No speaker notes for this slide.';
  }

  function show(nextIndex, replaceHash = false) {
    if (!slides.length) return;
    index = Math.min(slides.length - 1, Math.max(0, nextIndex));
    slides.forEach((slide, slideIndex) => slide.classList.toggle('active', slideIndex === index));
    if (counter) counter.textContent = `${index + 1} / ${slides.length}`;
    if (progress) progress.style.width = `${((index + 1) / slides.length) * 100}%`;
    updateNotes();
    const hash = `#${slides[index].id}`;
    if (location.hash !== hash) history[replaceHash ? 'replaceState' : 'pushState'](null, '', hash);
  }

  function fromHash() {
    const hash = decodeURIComponent(location.hash.slice(1));
    const hashIndex = slides.findIndex((slide) => slide.id === hash);
    show(hashIndex >= 0 ? hashIndex : index, true);
  }

  function setEditing(enabled) {
    document.body.classList.toggle('editing', enabled);
    document.querySelectorAll('.object[data-editable="true"] [data-edit-target="true"]').forEach((node) => {
      node.contentEditable = enabled ? 'true' : 'false';
    });
  }

  function downloadEditedDeck() {
    const clone = document.documentElement.cloneNode(true);
    clone.querySelector('body')?.classList.remove('editing');
    clone.querySelectorAll('[contenteditable]').forEach((node) => node.setAttribute('contenteditable', 'false'));
    const blob = new Blob([`<!doctype html>\n${clone.outerHTML}`], { type: 'text/html;charset=utf-8' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `${deckId}-edited.html`;
    link.click();
    setTimeout(() => URL.revokeObjectURL(link.href), 1000);
  }

  document.addEventListener('keydown', (event) => {
    if (event.target?.isContentEditable && !['Escape'].includes(event.key)) return;
    if (['ArrowRight', 'ArrowDown', 'PageDown', ' '].includes(event.key)) {
      event.preventDefault();
      show(index + 1);
    } else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(event.key)) {
      event.preventDefault();
      show(index - 1);
    } else if (event.key === 'Home') show(0);
    else if (event.key === 'End') show(slides.length - 1);
    else if (event.key.toLowerCase() === 'e') setEditing(!document.body.classList.contains('editing'));
    else if (event.key.toLowerCase() === 'n') notes?.classList.toggle('visible');
    else if (event.key.toLowerCase() === 'f') document.documentElement.requestFullscreen?.();
    else if (event.key.toLowerCase() === 'p') window.print();
    else if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 's') {
      event.preventDefault();
      downloadEditedDeck();
    } else if (event.key === 'Escape') {
      setEditing(false);
      notes?.classList.remove('visible');
    }
  });

  document.querySelector('[data-action="prev"]')?.addEventListener('click', () => show(index - 1));
  document.querySelector('[data-action="next"]')?.addEventListener('click', () => show(index + 1));
  document.querySelector('[data-action="notes"]')?.addEventListener('click', () => notes?.classList.toggle('visible'));
  document.querySelector('[data-action="edit"]')?.addEventListener('click', () => setEditing(!document.body.classList.contains('editing')));
  document.querySelector('[data-action="save"]')?.addEventListener('click', downloadEditedDeck);

  document.addEventListener('touchstart', (event) => { touchStartX = event.changedTouches[0]?.clientX ?? null; }, { passive: true });
  document.addEventListener('touchend', (event) => {
    if (touchStartX === null) return;
    const delta = (event.changedTouches[0]?.clientX ?? touchStartX) - touchStartX;
    if (Math.abs(delta) > 48) show(index + (delta < 0 ? 1 : -1));
    touchStartX = null;
  }, { passive: true });

  window.addEventListener('resize', scaleStage);
  window.addEventListener('hashchange', fromHash);
  scaleStage();
  fromHash();
})();
