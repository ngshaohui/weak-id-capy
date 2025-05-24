function toggleButton() {
  const checkbox = document.getElementById("confirm-reset-box").checked;
  if (checkbox === true) {
    document.getElementById("reset-btn").disabled = false;
  } else {
    document.getElementById("reset-btn").disabled = true;
  }
}
document.getElementById("confirm-reset-box").addEventListener("click", toggleButton);
