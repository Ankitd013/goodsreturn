let step = 'step1';

const step1 = document.getElementById('step1');
const step2 = document.getElementById('step2');
const step3 = document.getElementById('step3');
const step4 = document.getElementById('step4');
const step5 = document.getElementById('step5');
const step6 = document.getElementById('step6');
const step7 = document.getElementById('step7');

function next() {
  if (step === 'step1') {
    step = 'step2';
    step1.classList.remove("is-active");
    step1.classList.add("is-complete");
    step2.classList.add("is-active");

  } else if (step === 'step2') {
    step = 'step3';
    step2.classList.remove("is-active");
    step2.classList.add("is-complete");
    step3.classList.add("is-active");

  } else if (step === 'step3') {
    step = 'step4';
    step3.classList.remove("is-active");
    step3.classList.add("is-complete");
    step4.classList.add("is-active");

  } else if (step === 'step4') {
    step = 'step5';
    step4.classList.remove("is-active");
    step4.classList.add("is-complete");
    step5.classList.add("is-active");
  }
  else if (step === 'step5') {
    step = 'step6';
    step5.classList.remove("is-active");
    step5.classList.add("is-complete");
    step6.classList.add("is-active");
  }
  else if (step === 'step6') {
    step = 'step7d';
    step6.classList.remove("is-active");
    step6.classList.add("is-complete");
    step7.classList.add("is-active");
  }
  else if (step === 'step7d') {
    step = 'complete';
    step7.classList.remove("is-active");
    step7.classList.add("is-complete");
  }
  
}
