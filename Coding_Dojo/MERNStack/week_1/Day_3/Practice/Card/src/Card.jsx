function Card(props) {
    return (
        <div className="card">
            <h2>{props.name}</h2>
            <p>Age:{props.age}</p>
            <p>haircolor: {props.color}</p>

        </div>


    );

}



export default Card