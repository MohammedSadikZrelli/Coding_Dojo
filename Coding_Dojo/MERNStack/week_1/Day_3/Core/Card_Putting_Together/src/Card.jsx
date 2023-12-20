import React, {useState} from "react";
function Card(props) {
    const[age,setAge] =useState(props.age)
    const incrementAge=() => {
        setAge(age+1)
    }

    return (
        <div className="card">
            <h2>{props.name}</h2>
            <p>Age:{age}</p>
            <p>haircolor: {props.color}</p>
            <button onClick={incrementAge}>Happy Birthday</button>
          
        </div>


    );

}



export default Card