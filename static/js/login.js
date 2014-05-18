$(document).ready(
  function(){
    $("#login-form").submit(function(e){
    e.preventDefault();
    return false;
})});
function validate_form() {
  var uname=$("#inputUsername");
  var pword=$("#inputPassword");
  if(((uname.val().length) == 0) || ((pword.val().length) == 0)){
	  add_error("empty");
  }
  else
  {
	  var d = login();
  }
}
function add_error(type) {
	if(type=="empty") {
	    $("#ufg").addClass("has-error");
	    $("#pfg").addClass("has-error");
		$("#Result").text("用户名或密码不能为空").addClass("visible");
	}
	else if(type=="error"){
      $("#ufg").addClass("has-error");
	    $("#pfg").addClass("has-error");
		 $("#Result").text("用户名或密码错误").addClass("visible");
	}
}
function clean_form() {
	var uname=$("#inputUsername");
    var pword=$("#inputPassword");
	$("#ufg").removeClass("has-error");
	$("#pfg").removeClass("has-error");
	if($("#Result").hasClass("visible")){
	    uname.val("");
	    pword.val("");
	}
	$("#Result").val("").removeClass("visible");
}
function login() {
	$.ajax({
		async:false,
		url : "/accounts/login/",
		data : $('#login-form').serialize(),
		type:"POST",
		success: function(data) {
			if(data.status=="error") {add_error("error");}
			else {}
		},
	});
}