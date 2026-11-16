const eventCard = document.querySelector("#event");

eventCard.hidden = Date.now() >= Date.parse(eventCard.dataset.ends);

const motionToggle = document.querySelector("#motion-toggle");

motionToggle.hidden = false;
motionToggle.addEventListener("click", () => {
  const paused = document.body.toggleAttribute("data-motion-paused");
  motionToggle.textContent = paused ? "Resume background" : "Pause background";
});
