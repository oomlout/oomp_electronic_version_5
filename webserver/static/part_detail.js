document.addEventListener("DOMContentLoaded", () => {
  const panel = document.querySelector(".primary-preview-panel");
  if (!panel) return;
  const preview = panel.querySelector(".detail-preview");
  const original = panel.querySelector(".detail-preview-link");
  const strip = panel.querySelector(".diagram-gallery");
  const thumbnails = Array.from(panel.querySelectorAll("[data-diagram-thumbnail]"));
  const controls = Array.from(panel.querySelectorAll("[data-diagram-step]"));
  const status = panel.querySelector(".diagram-status");
  if (!preview || !original || !strip || !thumbnails.length) return;

  let active = thumbnails.findIndex((thumbnail) => thumbnail.href === original.href);
  const partName = preview.alt;
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  const markSelection = () => {
    thumbnails.forEach((thumbnail, index) => {
      thumbnail.setAttribute("aria-current", index === active ? "true" : "false");
    });
    status.textContent = active < 0 ? "Select a diagram" : `${active + 1} / ${thumbnails.length} · ${thumbnails[active].dataset.diagramTitle}`;
  };

  const showDiagram = (index, focus = false) => {
    active = (index + thumbnails.length) % thumbnails.length;
    const thumbnail = thumbnails[active];
    preview.removeAttribute("srcset");
    preview.removeAttribute("sizes");
    preview.src = thumbnail.dataset.previewUrl;
    preview.alt = `${thumbnail.dataset.diagramTitle} — ${partName}`;
    original.href = thumbnail.href;
    original.dataset.imageIndex = thumbnail.dataset.imageIndex;
    markSelection();
    if (focus) thumbnail.focus({ preventScroll: true });
    // Scroll only the strip, keeping the large preview in place.
    const bounds = strip.getBoundingClientRect();
    const card = thumbnail.getBoundingClientRect();
    const delta = card.left < bounds.left ? card.left - bounds.left : card.right > bounds.right ? card.right - bounds.right : 0;
    strip.scrollBy({ left: delta, behavior: reducedMotion.matches ? "auto" : "smooth" });
  };

  thumbnails.forEach((thumbnail, index) => {
    thumbnail.addEventListener("click", (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      showDiagram(index);
    });
    thumbnail.addEventListener("keydown", (event) => {
      const destinations = { ArrowLeft: index - 1, ArrowRight: index + 1, Home: 0, End: thumbnails.length - 1 };
      if (!(event.key in destinations)) return;
      event.preventDefault();
      showDiagram(destinations[event.key], true);
    });
  });
  controls.forEach((button) => {
    button.hidden = false;
    button.disabled = thumbnails.length < 2;
    button.addEventListener("click", () => {
      const step = Number(button.dataset.diagramStep);
      showDiagram(active < 0 ? (step > 0 ? 0 : thumbnails.length - 1) : active + step);
    });
  });
  markSelection();
});
