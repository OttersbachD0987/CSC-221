import sdl3_alias as sdl3

sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO)
window = sdl3.SDL_CreateWindow("Vi".encode(), 900, 900, sdl3.SDL_WINDOW_RESIZABLE)
renderer = sdl3.SDL_CreateRenderer(window, "Monk".encode())

rect = sdl3.SDL_FRect(255, 255, 15, 200)
event = sdl3.SDL_Event()

running = True

while running:
    while sdl3.SDL_PollEvent(event):
        if event == sdl3.SDL_EVENT_QUIT:
            running = False
    print("")
    sdl3.SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0)
    sdl3.SDL_RenderClear(renderer)
    sdl3.SDL_SetRenderDrawColor(renderer, 255, 0, 0, 0)
    sdl3.SDL_RenderFillRect(renderer, rect)
    
    sdl3.SDL_RenderPresent(renderer)
    sdl3.SDL_Delay(30)

sdl3.SDL_DestroyRenderer(renderer)
sdl3.SDL_DestroyWindow(window)
sdl3.SDL_Quit()