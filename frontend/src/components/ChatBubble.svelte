<script>
    import { onMount } from "svelte";

    export let phone, owner, index;
    let isOwner;
    let hasLastMessage;
    let hasNewMessage;
    let isLastMessage;

    $: if (phone.chats[index].owner == owner) {
        isOwner = true;
    } else {
        isOwner = false;
    }
    $: if (index > 0) {
        if (phone.chats[index].owner == phone.chats[index - 1].owner) {
            hasLastMessage = true;
        }
    }
    $: if (index < phone.chats.length - 1) {
        if (phone.chats[index].owner == phone.chats[index + 1].owner) {
            hasNewMessage = true;
            isLastMessage = false;
        } else {
            isLastMessage = true;
        }
    } else {
        isLastMessage = true;
    }
</script>

{#if phone.chats[index].type == 0}
    <div
        class="flex transition-all items-center px-3 py-[2px]"
        class:justify-end={owner == phone.chats[index].owner}
        class:mt-auto={index == 0}
        class:pb-2={index == phone.chats.length - 1}
    >
        {#if isOwner}
            <div
                class="p-1 px-4 bg-green-500 rounded-3xl max-w-[90%]"
                class:rounded-tr-lg={hasLastMessage}
                class:rounded-br-lg={hasNewMessage && !isLastMessage}
                class:rounded-br-none={isLastMessage}
            >
                {#if phone.encryptMode}
                    {phone.chats[index].encrypted}
                {:else}
                    {phone.chats[index].decrypted}
                {/if}
            </div>
        {:else}
            <div
                class="p-1 px-4 bg-gray-700 rounded-3xl max-w-[90%]"
                class:rounded-tl-lg={hasLastMessage}
                class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                class:rounded-bl-none={isLastMessage}
            >
                {#if phone.encryptMode}
                    {phone.chats[index].encrypted}
                {:else}
                    {phone.chats[index].decrypted}
                {/if}
            </div>
        {/if}
    </div>
{/if}
{#if phone.chats[index].type == 1}
    <div
        class="flex transition-all items-center px-3 py-[2px]"
        class:justify-end={owner == phone.chats[index].owner}
        class:mt-auto={index == 0}
        class:pb-2={index == phone.chats.length - 1}
    >
        {#if isOwner}
            <div
                class="border border-green-500 rounded-3xl max-w-[90%]"
                class:rounded-tr-lg={hasLastMessage}
                class:rounded-br-lg={hasNewMessage && !isLastMessage}
                class:rounded-br-none={isLastMessage}
            >
                {#if phone.encryptMode}
                    <img
                        class="rounded-3xl"
                        class:rounded-tr-lg={hasLastMessage}
                        class:rounded-br-lg={hasNewMessage && !isLastMessage}
                        class:rounded-br-none={isLastMessage}
                        src={phone.chats[index].encrypted}
                        alt=""
                    />
                {:else}
                    <img
                        class="rounded-3xl"
                        class:rounded-tr-lg={hasLastMessage}
                        class:rounded-br-lg={hasNewMessage && !isLastMessage}
                        class:rounded-br-none={isLastMessage}
                        src={phone.chats[index].decrypted}
                        alt=""
                    />
                {/if}
            </div>
        {:else}
            <div
                class="border border-gray-700 rounded-3xl max-w-[90%]"
                class:rounded-tl-lg={hasLastMessage}
                class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                class:rounded-bl-none={isLastMessage}
            >
                {#if phone.encryptMode}
                    <img
                        class="rounded-3xl"
                        class:rounded-tl-lg={hasLastMessage}
                        class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                        class:rounded-bl-none={isLastMessage}
                        src={phone.chats[index].encrypted}
                        alt=""
                    />
                {:else}
                    <img
                        class="rounded-3xl"
                        class:rounded-tl-lg={hasLastMessage}
                        class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                        class:rounded-bl-none={isLastMessage}
                        src={phone.chats[index].decrypted}
                        alt=""
                    />
                {/if}
            </div>
        {/if}
    </div>
{/if}
{#if phone.chats[index].type == 2}
    <div
        class="flex transition-all items-center px-3 py-[2px]"
        class:justify-end={owner == phone.chats[index].owner}
        class:mt-auto={index == 0}
        class:pb-2={index == phone.chats.length - 1}
    >
        {#if isOwner}
            <div
                class="border border-green-500 rounded-3xl max-w-[90%]"
                class:rounded-tr-lg={hasLastMessage}
                class:rounded-br-lg={hasNewMessage && !isLastMessage}
                class:rounded-br-none={isLastMessage}
            >
                {#if phone.encryptMode}
                    <video
                        controls
                        class="rounded-3xl"
                        class:rounded-tr-lg={hasLastMessage}
                        class:rounded-br-lg={hasNewMessage && !isLastMessage}
                        class:rounded-br-none={isLastMessage}
                        src={phone.chats[index].encrypted}
                        alt=""
                    ></video>
                {:else}
                    <video
                        controls
                        class="rounded-3xl"
                        class:rounded-tr-lg={hasLastMessage}
                        class:rounded-br-lg={hasNewMessage && !isLastMessage}
                        class:rounded-br-none={isLastMessage}
                        src={phone.chats[index].decrypted}
                    ></video>
                {/if}
            </div>
        {:else}
            <div
                class="border border-gray-700 rounded-3xl max-w-[90%]"
                class:rounded-tl-lg={hasLastMessage}
                class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                class:rounded-bl-none={isLastMessage}
            >
                {#if phone.encryptMode}
                    <video
                        controls
                        class="rounded-3xl"
                        class:rounded-tl-lg={hasLastMessage}
                        class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                        class:rounded-bl-none={isLastMessage}
                        src={phone.chats[index].encrypted}
                        alt=""
                    ></video>
                {:else}
                    <video
                        controls
                        class="rounded-3xl"
                        class:rounded-tl-lg={hasLastMessage}
                        class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                        class:rounded-bl-none={isLastMessage}
                        src={phone.chats[index].decrypted}
                        alt=""
                    ></video>
                {/if}
            </div>
        {/if}
    </div>
{/if}
{#if phone.chats[index].type == 3}
    <div
        class="flex transition-all items-center px-3 py-[2px]"
        class:justify-end={owner == phone.chats[index].owner}
        class:mt-auto={index == 0}
        class:pb-2={index == phone.chats.length - 1}
    >
        {#if isOwner}
            <div
                class="border border-green-500 bg-green-500 rounded-3xl max-w-[90%]"
                class:rounded-tr-lg={hasLastMessage}
                class:rounded-br-lg={hasNewMessage && !isLastMessage}
                class:rounded-br-none={isLastMessage}
            >
                {#if phone.encryptMode}
                    <audio
                        controls
                        class="rounded-3xl"
                        class:rounded-tr-lg={hasLastMessage}
                        class:rounded-br-lg={hasNewMessage && !isLastMessage}
                        class:rounded-br-none={isLastMessage}
                        src={phone.chats[index].encrypted}
                        alt=""
                    ></audio>
                {:else}
                    <audio
                        controls
                        class="rounded-3xl"
                        class:rounded-tr-lg={hasLastMessage}
                        class:rounded-br-lg={hasNewMessage && !isLastMessage}
                        class:rounded-br-none={isLastMessage}
                        src={phone.chats[index].decrypted}
                    ></audio>
                {/if}
            </div>
        {:else}
            <div
                class="border border-gray-700 bg-grey-700 rounded-3xl max-w-[90%]"
                class:rounded-tl-lg={hasLastMessage}
                class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                class:rounded-bl-none={isLastMessage}
            >
                {#if phone.encryptMode}
                    <audio
                        controls
                        class="rounded-3xl"
                        class:rounded-tl-lg={hasLastMessage}
                        class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                        class:rounded-bl-none={isLastMessage}
                        src={phone.chats[index].encrypted}
                        alt=""
                    ></audio>
                {:else}
                    <audio
                        controls
                        class="rounded-3xl"
                        class:rounded-tl-lg={hasLastMessage}
                        class:rounded-bl-lg={hasNewMessage && !isLastMessage}
                        class:rounded-bl-none={isLastMessage}
                        src={phone.chats[index].decrypted}
                        alt=""
                    ></audio>
                {/if}
            </div>
        {/if}
    </div>
{/if}

<style>
    audio::-webkit-media-controls-panel {
        background-color: transparent;
    }
</style>
