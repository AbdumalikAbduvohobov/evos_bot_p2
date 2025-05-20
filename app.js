let tg = window.Telegram.WebApp;
tg.expand();
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#af0808";

 // 1- Mahsulot
let count_1 = 0;
let count1 = document.getElementById("count1");
let addbtn1 = document.getElementById("addbtn1");
let rbtn1 = document.getElementById("rbtn1");

addbtn1.addEventListener("click", function (){
	count1.innerText = count_1 += 1;
	tg.MainButton.setText("To'lov");
	tg.MainButton.show();
});
rbtn1.addEventListener("click", function (){
	if (count_1 > 0) {
		count1.innerText = count_1 -= 1;
	}
	if (count_1 === 0){
		tg.MainButton.hide();
	}

});

// 2-Mahsulot