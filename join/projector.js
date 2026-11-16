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
  const updateFullscreenLabel = () => {
    const label = document.fullscreenElement ? "Exit fullscreen" : "Enter fullscreen";
    fullscreenToggle.setAttribute("aria-label", label);
    fullscreenToggle.title = label;
  };

  fullscreenToggle.hidden = false;
  updateFullscreenLabel();
  document.addEventListener("fullscreenchange", updateFullscreenLabel);

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
