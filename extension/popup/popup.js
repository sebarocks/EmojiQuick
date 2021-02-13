let emojiStr = "";

function clicking(evt) {
  nuevoEmoji = evt.target.textContent;
  console.log(evt.target.textContent);
  emojiStr = emojiStr.concat(nuevoEmoji);
  navigator.clipboard.writeText(emojiStr)
    .then(
      () => { document.querySelector("#emojistr").textContent = emojiStr; }

    );
  console.log(twemoji.parse('I \u2764\uFE0F emoji!', { base: "/emojis/" }));
  document.querySelector("#twemoji").innerHTML = twemoji.parse('I \u2764\uFE0F emoji!', { base: "/emojis/" });

}

document.querySelectorAll(".test")
  .forEach(e => e.addEventListener("click", clicking));