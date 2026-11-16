const eventCard = document.querySelector("#event");

eventCard.hidden = Date.now() >= Date.parse(eventCard.dataset.ends);

const motionToggle = document.querySelector("#motion-toggle");

motionToggle.hidden = false;
motionToggle.addEventListener("click", () => {
  const paused = document.body.toggleAttribute("data-motion-paused");
  motionToggle.textContent = paused ? "Resume background" : "Pause background";
});

const fullscreenToggle = document.querySelector("#fullscreen-toggle");

if (document.fullscreenEnabled) {
  const page = document.documentElement;
  let cursorTimeout;

  const resetCursor = () => {
    clearTimeout(cursorTimeout);
    page.removeAttribute("data-cursor-idle");

    if (document.fullscreenElement === page) {
      cursorTimeout = setTimeout(() => page.setAttribute("data-cursor-idle", ""), 2000);
    }
  };

  const syncFullscreen = () => {
    const label = document.fullscreenElement ? "Exit fullscreen" : "Enter fullscreen";
    fullscreenToggle.setAttribute("aria-label", label);
    fullscreenToggle.title = label;
    resetCursor();
  };

  fullscreenToggle.hidden = false;
  syncFullscreen();
  document.addEventListener("fullscreenchange", syncFullscreen);
  document.addEventListener("pointermove", () => {
    if (document.fullscreenElement === page) resetCursor();
  }, { passive: true });

  fullscreenToggle.addEventListener("click", async () => {
    try {
      if (document.fullscreenElement) {
        await document.exitFullscreen();
      } else {
        await document.documentElement.requestFullscreen();
      }
    } catch (error) {
      console.warn("Could not change fullscreen mode", error);
    }
  });
}
