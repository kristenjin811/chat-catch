import data from '@emoji-mart/data'
import Picker from '@emoji-mart/react'


export default function EmojiPicker() {
  return (
    <div>
      <Picker data={data} onEmojiSelect={console.log} />
    </div>
  )
}
