console.log("its working");

const btns = [...document.getElementsByClassName('copy')]

console.log(btns);

btns.forEach(btn=> btn.addEventListener('click', ()=>{
    console.log('click clicked')
}))

