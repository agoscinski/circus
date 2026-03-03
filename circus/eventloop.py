import asyncio

def get_or_create_event_loop() -> asyncio.AbstractEventLoop:
    """Get the running event loop, or the current set loop, or create and set a new one.
    Note: aiida should never call on asyncio.get_event_loop() directly.
    """
    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        pass
    try:
        # See issue https://github.com/aiidateam/plumpy/issues/336
        loop = asyncio.get_event_loop()
        if not loop.is_closed():
            return loop
    except RuntimeError:
        pass
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop
