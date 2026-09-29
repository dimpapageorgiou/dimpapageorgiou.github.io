document.querySelectorAll(".formatted-number").forEach((element) => {
  const value = Number(element.dataset.number);

  if (!Number.isNaN(value)) {
    element.textContent = value.toLocaleString("en-US");
  }
});