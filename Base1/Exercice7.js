function ex7 (){
    var pointure= parseInt(prompt("Quel est votre pointure?"));
    var annN=parseInt(prompt("Quel est votre année de naissance?"));
    x=(((((pointure*2)+5)*50)-annN)+1766);
    alert(x);
}
ex7()