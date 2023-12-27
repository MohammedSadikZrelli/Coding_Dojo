import React, {useState} from 'react'
function ToDoList(){
    const [tasks,setTasks] = useState(["eat breakfast","take a shower","walk the dog"]);
    const [newTask,setNewTask] = useState("");
    function handleInputChange(event){
        setNewTask(event.target.value)

    }

    function addTask() {
        setTasks(t=> [...tasks,newTask])
        setNewTask("");
    }
    function deleteTask(index) {

    }
    function moveTaskUp(index){

    }

    function moveTaskdown(index){

    }

return (<div className='to-do-list'>
    <h1>To-Do-List</h1>
    <div>
        <input type="text"
        placeholder='Enter a task...'
        value={newTask} 
        onChange={handleInputChange}  />
        <button 
        className='add-button' 
        onClick={addTask}>
            add

        </button>
    </div>
    <ol>
        {tasks.map((task,index)=> 
        <li key={index}><span className='text'>{task}</span>
        
        <button
        className='delete-button'
        onClick={()=>deleteTask(index)}>
            delete</button>
            <button
        className='move-button'
        onClick={()=>moveTaskUp(index)}>
            UP </button>
            <button
        className='down-button'
        onClick={()=>moveTaskdown(index)}>
            down</button>
        </li>
            
        )}
    </ol>

</div>)

}
export default ToDoList