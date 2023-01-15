window.onload=function(){
    var auto = setTimeout(function(){ autoRefresh(); }, 100);

    function submitform(){
      document.forms["WorkForm"].submit();
    }

    function autoRefresh(){
       clearTimeout(auto);
       auto = setTimeout(function(){ submitform(); autoRefresh(); }, 10000);
    }
}