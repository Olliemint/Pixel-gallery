console.log("try again");


function copyclipboard() {
    var copyText = document.getElementById('link')
    copyText.select();
    document.execCommand('copy')
    alert(`Copied clipboard`);
  }