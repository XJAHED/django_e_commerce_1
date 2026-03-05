function duplicate_email(email){
    var url = `/authentication/duplicate_email/?email=${email}`
     $.ajax({
        url:url,
        type:"GET",
        success:function(response){
            if(response.status==409){
                document.getElementById('email_error').classList.remove("d-none")
            }else{
                document.getElementById('email_error').classList.add("d-none")
            }
        }
     })
}

function checkPassword (){
    if (document.getElementById('password').value == document.getElementById('confirm_password').value){
        document.getElementById('pass_check').innerHTML = ' <p style="color: green;">Matching</p>';
    }else{
        document.getElementById('pass_check').innerHTML = ' <p style="color: red;">Passwords do not match</p>';
    }
}