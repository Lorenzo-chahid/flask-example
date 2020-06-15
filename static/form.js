let name = document.getElementById('name');
let surname = document.getElementById('surname');
let email = document.getElementById('email');
let form = document.getElementById('form');
let submit = document.getElementById('submit');
let send_mail = document.getElementById("send_email")
const mdp = document.getElementById('mdp')
const mdp_confirm = document.getElementById('mdp_confirm')



const logo_send = document.getElementById("logo_send")


// REGEX 
const regex_name = /^[a-zA-Z]+$/
// regex to increase 
const regex_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/ ;
const regex_mdp = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/ ; 

// MESSAGE ERROR
const error_name = document.getElementById('error_name');
const error_email = document.getElementById('error_email');
const error_mdp = document.getElementById('error_mdp');
const error_mdp_confirm = document.getElementById('error_mdp_confirm');

(()=>{

    form.addEventListener('submit', (e)=>{
        if(name.value == '' || name.value == null){
            error_name.innerHTML= "Merci d'entrer un nom !"
            e.preventDefault();
          
        }else if(name.value.length < 3 || name.value.length > 10){
            error_name.innerHTML= "Nom trop court ou trop long...";
            e.preventDefault();
        }else if(!regex_name.test(name.value)){
            error_name.innerHTML= "Merci de n'entrer que des lettres !";
            e.preventDefault();

        }else{
            const name_valid = false
        }
        
        if(surname.value == '' || surname.value == null){
            error_surname.innerHTML= "Merci d'entrer un nom !";
            e.preventDefault();
          
        }else if(surname.value.length < 3 || surname.value.length > 10){
            error_surname.innerHTML= "Nom trop court ou trop long...";
            e.preventDefault();
        }else if(!regex_name.test(surname.value)){
            error_surname.innerHTML= "Merci de n'entrer que des lettres !";
            e.preventDefault();

        }
        else{
            const surname_valid = false
        }

        if(email.value == "" || email.value == null){
            error_email.innerHTML="Veuillez mettre un email";
        }else if(email.value.length < 7 || email.value.length > 30){
            error_email.innerHTML="votre email est trop court ou trop long";
        }else if(!regex_email.test(email.value)){
            error_email.innerHTML="Veuillez entrer un mail valide !"
        }else{
            const email_valid = false
        }

        if(mdp.value == "" || mdp.value == null){
            error_mdp.innerHTML="Veuillez mettre un mdp";
        }else if(mdp.value.length < 7 || mdp.value.length > 30){
            error_mdp.innerHTML="votre mdp est trop court ou trop long";
        }else if(!regex_mdp.test(mdp.value)){
            error_mdp.innerHTML="Veuillez entrez un mot de passe avec majuscule et minuscule!"
        }else{
            const mdp_valid = false
        }

        if(mdp.value == "" || mdp.value == null){
            error_mdp.innerHTML="Veuillez mettre un mdp";
        }else if(mdp.value.length < 7 || mdp.value.length > 30){
            error_mdp.innerHTML="votre mdp est trop court ou trop long";
        }else if(!regex_mdp.test(mdp.value)){
            error_mdp.innerHTML="Veuillez entrez un mot de passe avec majuscule et minuscule!"
        }

        if(mdp_confirm.value == "" || mdp_confirm.value == null){
            error_mdp_confirm.innerHTML="Veuillez mettre un mdp";
           
        }else if(mdp_confirm.value != mdp){
            error_mdp_confirm.innerHTML="Veuillez entrer les mêmes mots de passes"
        }else{
            const mdp_confirm_valid = false
        }

        if(name_valid == false && surname_valid==false && email_valid==false &&mdp_valid==false){
            logo_send.style.transform ="translatex(900px) "
            submit.style.backgroundImage="linear-gradient(315deg, #3bb78f 0%, #0bab64 74%)";
            submit.innerHTML="envoyé ;)";
            e.preventdefault();
        }

     


        e.preventdefault();
           
            


    })

  


      


let test_name = /^[a-z]^/

})();
