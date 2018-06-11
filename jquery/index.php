<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>


<script>
$(document).ready(function(){
from=document.getElementById("from").value;
to=document.getElementById("to").value;
        $.post("http://127.0.0.1:8000/ajax",
        {
          from: from,
          to: to
        },
        function(data,status){
	    document.getElementById("demo").innerHTML=data;
        });

});
</script>

<script>
$(document).ready(function(){
    $("button").click(function(){
from=document.getElementById("from").value;
to=document.getElementById("to").value;
        $.post("http://127.0.0.1:8000/ajax",
        {
          from: from,
          to: to,
	  fix:0
        },
        function(data,status){
	    document.getElementById("demo").innerHTML=data;
        });

    });
});
</script>
  <script>
  $( function() {
    var dateFormat = "yy/mm/dd",
      from = $( "#from" )
        .datepicker({
          defaultDate: "+1w",
          changeMonth: true,
          numberOfMonths: 3
        })
        .on( "change", function() {
          to.datepicker( "option", "minDate", getDate( this ) );
        }),
      to = $( "#to" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 3
      })
      .on( "change", function() {
        from.datepicker( "option", "maxDate", getDate( this ) );
      });
 
    function getDate( element ) {
      var date;
      try {
        date = $.datepicker.parseDate( dateFormat, element.value );
      } catch( error ) {
        date = null;
      }
 
      return date;
    }
  } );
  </script>
</head>
<body>

<button type="button">Send</button>
<br><br>

<label for="from">From</label>
<input type="text" id="from" name="from" value="<?php echo date("Y-m-1");?>">
<label for="to">to</label>
<input type="text" id="to" name="to" value="<?php echo date("Y-m-d");?>">

<div id="demo"></div>

</body>
</html>
