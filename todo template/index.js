let circularProgress = document.querySelector(".circular-progress"),
progressValue = document.querySelector(".progress-value");
const todoCount = document.getElementsByClassName('count').length;
console.log(todoCount)


let progressStartValue = 100;    
let progressEndValue = 0;
let speed = 100;

const progress = setInterval(() => {
progressStartValue = (todoCount / 25) * 100 ;

progressValue.textContent = `${100 - progressStartValue}%`
circularProgress.style.background = `conic-gradient(#7d2ae8 ${(100 - progressStartValue) * 3.6}deg, #ededed 0deg)`

if(progressStartValue == progressEndValue){
    clearInterval(progress);
}    
}, speed);