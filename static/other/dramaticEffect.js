const text = "Thank you";
const ominousMsg = document.getElementById("endText"); 
ominousMsg.innerHTML = "";

let i = 0;
const speed = 500;

function DramaticTyping() {
    if (i < text.length) {
        ominousMsg.innerHTML += text[i];
        i++;
        setTimeout(DramaticTyping, speed);
    }
}

setTimeout(DramaticTyping, 3000);