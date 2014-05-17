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
	else {
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
		url : "",
		dataType: "json",
		data : $('#login-form').serialize(),
		success: function(data) {
			return data;
		}
	});
}