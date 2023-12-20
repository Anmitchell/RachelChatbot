import { useState } from 'react'
import { FiRefreshCw } from 'react-icons/fi'
import axios from 'axios'

type Props = {
  setMessages: any
}

function Title({ setMessages }: Props) {
  const [isResetting, setIsResetting] = useState(false)

  // Reset the conversation
  const resetConversation = async () => {
    setIsResetting(true)

    // Make request to backend route to reset conversation
    await axios
      .get('http://localhost:8000/reset')
      .then((res) => {
        if (res.status == 200) {
          setMessages([])
        } else {
          console.error('There was an error with the API request to backend.')
        }
      })
      .catch((err) => {
        console.error(err.message)
      })

    setIsResetting(false)
  }

  return (
    <div className='flex justify-between items-center w-full p-4 bg-gray-900 text-white font-bold shadow'>
      <div className='italic'>Rachel</div>
      <button
        className={
          'transition-all duration-300 text-blue-300 hover:text-pink-500 ' +
          (isResetting && 'animate-pulse')
        }
        onClick={resetConversation}
      >
        <FiRefreshCw size={25} />
      </button>
    </div>
  )
}

export default Title
