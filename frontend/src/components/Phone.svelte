<script>
    import Phone from "./Phone.svelte";
    import ChatBar from "./ChatBar.svelte";
    import StatusBar from "./StatusBar.svelte";
    import ChatBubble from "./ChatBubble.svelte";
    let chatList;
    export let owner, phone, otherOwner;
</script>

<div class="relative w-[400px] h-[765px]">
    <img
        src="/phone_border.png"
        class="w-full absolute scale-105 pointer-events-none"
        alt=""
    />
    <div class="bg-gray-800 w-full h-full rounded-3xl px-4 py-1">
        <StatusBar />
        <div class="grid grid-cols-5 border-b border-b-gray-600 pb-2">
            <div></div>
            <div class="col-span-3">
                <h1 class="text-center text-md font-bold">{owner}</h1>
                <h2 class="text-center text-xs text-blue-400">Online</h2>
            </div>
            <div></div>
        </div>
        <div class="h-[600px] overflow-y-scroll chat-list" id={owner}>
            <ul class="flex flex-col h-full transition-all">
                {#each phone.chats as chat, i}
                    <ChatBubble bind:phone bind:owner index={i} />
                {/each}
            </ul>
        </div>
        <ChatBar bind:phone bind:owner bind:otherOwner />
    </div>
</div>

<style>
    /* width */
    .chat-list::-webkit-scrollbar {
        width: 4px;
    }

    /* Track */
    .chat-list::-webkit-scrollbar-track {
        background: #111827;
    }
    .chat-list::-webkit-scrollbar-track:hover {
        background: #181e2c;
    }

    /* Handle */
    .chat-list::-webkit-scrollbar-thumb {
        background: #374151;
    }

    /* Handle on hover */
    .chat-list::-webkit-scrollbar-thumb:hover {
        background: #616972;
    }
</style>
