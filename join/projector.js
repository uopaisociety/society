const eventCard = document.querySelector("#event");

eventCard.hidden = Date.now() >= Date.parse(eventCard.dataset.ends);

const motionToggle = document.querySelector("#motion-toggle");

motionToggle.hidden = false;
motionToggle.addEventListener("click", () => {
  const paused = document.body.toggleAttribute("data-motion-paused");
  motionToggle.textContent = paused ? "Resume background" : "Pause background";
});

const fullscreenToggle = document.querySelector("#fullscreen-toggle");

const page = document.documentElement;
let cursorTimeout;

function resetCursor() {
  clearTimeout(cursorTimeout);
  page.removeAttribute("data-cursor-idle");

  if (document.fullscreenElement === page) {
    cursorTimeout = setTimeout(() => page.setAttribute("data-cursor-idle", ""), 2000);
  }
}

function syncPresentation() {
  const active = document.fullscreenElement === page || page.hasAttribute("data-scan-view");
  const label = active ? "Exit scan view" : "Enter fullscreen";
  fullscreenToggle.setAttribute("aria-label", label);
  fullscreenToggle.title = label;
  resetCursor();
}

function setScanView(active) {
  page.toggleAttribute("data-scan-view", active);
  syncPresentation();
}

fullscreenToggle.hidden = false;
syncPresentation();
document.addEventListener("fullscreenchange", syncPresentation);
document.addEventListener("pointermove", () => {
  if (document.fullscreenElement === page) resetCursor();
}, { passive: true });
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && page.hasAttribute("data-scan-view")) setScanView(false);
});

fullscreenToggle.addEventListener("click", async () => {
  if (page.hasAttribute("data-scan-view")) {
    setScanView(false);
    return;
  }

  if (document.fullscreenElement === page) {
    await document.exitFullscreen();
    return;
  }

  if (document.fullscreenEnabled) {
    try {
      await page.requestFullscreen();
      return;
    } catch {
      // Keep the large QR available if the browser declines native fullscreen.
    }
  }
  setScanView(true);
});
