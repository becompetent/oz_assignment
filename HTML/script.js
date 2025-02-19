//console.log('hello world');
//console.log(1+3)
//let num1 =10
//let num2 =15

//유저가 버튼을 클릭했을 대 특정한 함수가(동작이) 실행되도록 만들고 싶다.
const btn = document.querySelector('butoon')
console.log(btn);

// addEventListner는 2개의 전달인자를 찾는다
//1. 이벤트의 종류
//2. 실행할 함수
btn.addEventListener('click', funtion () {
    console.log('버튼클릭');
})