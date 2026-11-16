const fileInput = document.querySelector("#qr-file");
const invite = document.querySelector("#invite");
const setup = document.querySelector("#setup");
const change = document.querySelector("#change");
const status = document.querySelector("#status");
const eventCard = document.querySelector("#event");

eventCard.hidden = Date.now() >= Date.parse(eventCard.dataset.ends);

const openPicker = () => fileInput.click();
document.querySelector("#load").addEventListener("click", openPicker);
change.addEventListener("click", openPicker);

let currentImage;

fileInput.addEventListener("change", async () => {
  const [file] = fileInput.files;
  fileInput.value = "";
  if (!file) return;

  if (file.type !== "image/png" || file.size > 2_000_000) {
    status.textContent = "Choose the WhatsApp QR PNG (under 2 MB).";
    return;
  }

  const imageUrl = URL.createObjectURL(file);
  const preview = new Image();
  preview.src = imageUrl;

  try {
    await preview.decode();
    if (preview.naturalWidth !== preview.naturalHeight) {
      throw new Error("Expected a square QR image");
    }
  } catch {
    URL.revokeObjectURL(imageUrl);
    status.textContent = "Choose a valid square WhatsApp QR PNG.";
    return;
  }

  if (currentImage) URL.revokeObjectURL(currentImage);
  currentImage = imageUrl;
  invite.src = currentImage;
  invite.hidden = false;
  setup.hidden = true;
  change.hidden = false;
  status.textContent = "";
});
