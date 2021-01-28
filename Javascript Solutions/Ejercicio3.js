var array = [parseInt(Math.random() * 11),parseInt(Math.random() * 11),parseInt(Math.random() * 11),parseInt(Math.random() * 11),parseInt(Math.random() * 11)];

console.log("Entrada: "+array)
function sumarElementos(elementos){
    for (var i=0;i<elementos.length;i++){
        if (i>0){
            elementos[i] += elementos[(i-1)];
        }
    }
    console.log("Salida: "+elementos);
}

sumarElementos(array);