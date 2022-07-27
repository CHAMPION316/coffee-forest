const toastBtnRef = document.querySelector("#toastbtn")
toastBtnRef.addEventListener("click",()=>{
    const toastElList = [].slice.call(document.querySelectorAll('.toast'))
    const options = {delay: 3000}
    toastElList.map(function(toastEl) {
      return new bootstrap.Toast(toastEl, options)
    })
})