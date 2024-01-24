const funcao = array =>{
    return (array.length>3)? array.slice(3): [];
}
console.log(funcao([0,1,2,3,4,5,6]));
console.log(funcao([0,1,2]));
console.log(funcao([0,1,2,3,4]));
console.log(funcao([0]));