const eventCard = document.querySelector("#event");

eventCard.hidden = Date.now() >= Date.parse(eventCard.dataset.ends);
