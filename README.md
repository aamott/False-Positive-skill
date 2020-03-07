# False Positive Skill - ONLY WORKS WITH MODIFIED MYCROFT-CORE CODE
## About
This skill will only work if lines 547-573 of ~/mycroft-core/mycroft/client/speech/mic.py read:
                # Save positive wake words as appropriate
                if said_wake_word:
                    SessionManager.touch()
                    payload = {
                        'utterance': self.wake_word_name,
                        'session': SessionManager.get().session_id,
                    }
                    

                    audio = None
                    mtd = None
                    if self.save_wake_words:
                        # Save wake word locally
                        audio = self._create_audio_data(byte_data, source)
                        mtd = self._compile_metadata()
                        module = self.wake_word_recognizer.__class__.__name__

                        fn = join(
                            self.saved_wake_words_dir,
                            '_'.join(str(mtd[k]) for k in sorted(mtd)) + '.wav'
                        )
                        with open(fn, 'wb') as f:
                            f.write(audio.get_wav_data())
                        # add the last written wakeword recording
                        payload["filepath"] = fn

                    emitter.emit("recognizer_loop:wakeword", payload)
These lines add the file path of any wakeword recordings to the message sent by the listener. Without this, there is no way to see what the last file written was. 
This is to be used when trying to increase the accuracy of a wake word through retraining. If, in mycroft.conf, you have
    "save_wake_words": true,
    "record_wake_words": true
it will take the last recording and move it into a subdirectory of save_path called "not-wake-word"

## Examples
* "That was a false positive"
* "You should not have woken up"

## Credits
Bret Padres (for making a simple skill usable as an outline)
Adam (just converted it into something totally different)

## Category
**Debugging**

## Tags
#wake-word
#listener

