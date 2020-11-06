var left;
var fail;
var time ;
var startD, leftS, failS, timeS, messageD, lastMessage;
var randNum;  // 정답 이미지 위치가 담긴 배열
var img;  // 정답 이미지객체가 담긴 배열

function getId(){
	startD = document.getElementById("start_d");
	leftS = document.getElementById("left_s");
	failS = document.getElementById("fail_s");
	timeS = document.getElementById("time_s");
	messageD = document.getElementById("message_d");
	lastMessage = document.getElementById("continueGameMessage");
}

function clickSound(){
	var audio = document.getElementById("playAudio");
	audio.src = "click.mp3";
	audio.play();
}

function clearSound(){
	var audio = document.getElementById("playAudio");
	audio.src = "applause.mp3";
	audio.play();
}

function falseSound(){
	var audio = document.getElementById("playAudio");
	audio.src = "fail.mp3";
	audio.play();
}

function reset(){
// 초기 상태값, 이미지 초기화 
// 게임이 끝난 후 사용자가 게임 시작을 클릭하면 모든 state를 reset하여 다시 게임을 시작할 수 있음 
	left = 8;
	fail = 0;
	time = 16;
	randNum = [];
	img = []; 
	getId();
	for(var i=1; i<=24; i++){ 
		document.getElementById(eval("'"+i+"'")).src = "egg.png";
		document.getElementById(eval("'"+i+"'")).style.border = "none";
	}
	document.getElementById("gameOverMessage").style.display = "none";
	lastMessage.style.display = "none";
	
}
function startGame(){
	reset();
	for(var i=1; i<=24; i++){  // 게임 시작 버튼 누른 후 이미지 클릭 활성화
		document.getElementById(eval("'"+i+"'")).style.pointerEvents = "auto";
	}
	leftS.innerHTML = left;
	failS.innerHTML = fail;
	startD.style.display = "none";
	timeS.innerHTML = "남은 시간  " + time;
	messageD.innerHTML = "숨은 그림을 보세요";

	// 랜덤으로 1에서 24중 중복없이 8개의 번호 뽑기
	for(var i=0; i<8; i++){
		randNum[i] = Math.floor(Math.random() * 24 + 1); 
		for(var j=0; j<i; j++){
			if(randNum[i] == randNum[j]){
				i--;
				break;
			}
		}
		
	}

	// 해당 번호의 아이디값의 이미지 바꿔서 보여주기
	for(var i=0; i<8; i++){
		img[i] = document.getElementById(eval("'"+randNum[i]+"'"));
	}

	for(var i=0; i<8; i++){
		img[i].src = "dog.png";
	}

	// 정답이미지 보여준 후 3초 후 정답이미지 숨기기
	setTimeout(function(){
		showImg();
	}, 3000);

	messageD.innerHTML = "정답을 찾으세요";

	if (time <= 0){
		gameOver();
	}

	// 마찬가지로 3초 후부터 시간이 가도록 설정
	setTimeout(runTimer, 3000);
}

function showImg(){
	for(var i=0; i<8; i++){
		img[i].src = "egg.png";
	}
}

 // 타이머 설정 
 // 1초 간격으로 코드 실행	
 function runTimer(){
 	if (time <= 0){
		gameOver();
	}
	var timer = setInterval(function (){
		time--;
		timeS.innerHTML = "남은 시간  " + time;

		if(time < 0){
			clearInterval(timer);
			gameOver();
		}

		if(time >= 0 && left == 0){
			clearInterval(timer);
			gameClear();
		}		
	}, 1000);

	//clearInterval(timer);
 }

function playGame(obj){
	// message 바꾸기
	// 클릭 -> 맞는 번호면 이미지 바꾸기, 남은수-1
	// -> 틀리면 실패수 +1
	// 남은시간 줄어들기 

	clickSound();
	getId();
	if(img.includes(obj)){
		obj.src = "dog.png";
		left--;
		leftS.innerHTML = left;

		// gameOver에서 남은 이미지 보여주어야 하므로 배열에서 클릭한 정답이미지 삭제
		var idx = img.indexOf(obj);
		if(idx > -1){
			img.splice(idx, 1);
		}
	}
	else{
		fail++;
		failS.innerHTML = fail;
	}
	
 }

 function gameClear(){
 	clearSound();
 	getId();
 	document.getElementById("gameOverMessage").innerHTML = "GAME CLEAR!!";
 	document.getElementById("gameOverMessage").style.display = "block";
 	messageD.innerHTML = "성공!";
 	startD.style.display = "";
 	lastMessage.style.display = "block";
 	lastMessage.innerHTML = "게임을 다시 시작하려면 게임시작 버튼을 클릭하세요!";
 }

function gameOver(){
	// 남은 시간 == 0 이면 게임 실패 
	// GAME OVER 글씨와 남은 이미지 보여주기
	// message 실패
	falseSound();
	getId();
	timeS.innerHTML = "남은 시간  " + 0;
	messageD.innerHTML = "실패";
	document.getElementById("gameOverMessage").style.display = "block";
	document.getElementById("gameOverMessage").innerHTML = "GAME OVER!!";
	for(var i=0; i<img.length; i++){
		img[i].style.border = "3px solid red"
		img[i].src = "dog.png";
	}

	// 게임시작 버튼 보이게 하기 -> 다시 시작 가능
	startD.style.display = "";
	lastMessage.style.display = "block";
	lastMessage.innerHTML = "게임을 다시 시작하려면 게임시작 버튼을 클릭하세요!";
}

