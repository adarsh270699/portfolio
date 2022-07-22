import './App.css';
import img from '../src/javascript_illustration.svg'
function App() {
  return (
    <div className="App h-screen min-h-screen text-zinc-600">
      <div className="h-full flex flex-wrap justify-center content-center">
        <div className='sm:h-72 sm:w-96 h-64 w-72 bg-white shadow-sm hover:bg-gray-600 hover:text-white transition duration-500 rounded-xl p-10 space-y-5'>
          <img src={img} alt='img'></img>
          <h1 className='font-bold text-3xl text-center'>Site under construction!</h1>
        </div>
      </div>
    </div>
  );
}

export default App;
