from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
  #"65.2.69.37",
  "localhost",
  25565,
  #lang="en",
  translate=True,
  model="medium.en",
  use_vad=True
  )

client()