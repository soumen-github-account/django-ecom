const imgs =document.querySelectorAll('.header-slider ul img');
const prev_btn =document.querySelector('.control_prev');
const next_btn =document.querySelector('.control_next');
let n =0;
 
function changeSlide(){
    for(let i= 0; i< imgs.length;i++){
        imgs[i].style.display = 'none';
    }
    imgs[n].style.display = 'block';
}

prev_btn.addEventListener('click', (e)=>{
    if(n>0){
        n--;
    }
    else{
        n=imgs.length - 1;
    }
    changeSlide();
})

next_btn.addEventListener('click', (e)=>{
    if(n<imgs.length - 1){
        n++;
    }
    else{
        n=0;
    }
    changeSlide();
})
changeSlide();

const scrollContainer = document.querySelectorAll('.products');

for(const item of scrollContainer){
    item.addEventListener('wheel', (evt)=>{
        evt.preventDefault();
        item.scrollLeft += evt.deltaY;
    })
}


    const slides = document.querySelectorAll(".slid");

    slides.forEach((slid,index)=>{
        slid.style.left = `${index*100}%`;
    });
    
    let l = slides.length;
    const bottom = document.querySelector(".bottom");
    for(let i=1; i<=l;i++){
        const div =document.createElement('div');
        div.className = 'button';
        bottom.appendChild(div);
    };
    const buttons = document.querySelectorAll(".button");
    let count = 0;
    const slideImage = ()=>{
        slides.forEach(
            (slid)=>{
                slid.style.transform = `translateX(-${count*100}%)`;
            }
        )
    }
    
    const gonext =()=>{
        count++;
        
        slideImage();
    }
    const getfirst=()=>{
        slides.forEach(
            (slid)=>{
                slid.style.transform = `translateX(-0%)`;
            }
        )
        count = 0;
    }
    
    let slideIntarval;
    const start=()=>{
        slideIntarval=setInterval(()=>{
        count < l-1 ? gonext():getfirst();
        colorchange();
    },2000);
    
    };
    start();
    buttons[0].style.background='white';
    const resetBg=()=>{
        buttons.forEach(
            (button)=>{
                button.style.background='grey';
            }
        )
    }
    
    const colorchange=()=>{
        resetBg();
        buttons[count].style.background='white';
    };