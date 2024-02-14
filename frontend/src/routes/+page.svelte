<script>
    import Phone from "../components/Phone.svelte";
    let phone = {
        key: "asdbgffdmsestuiu",
        c1Prime: "",
        c2Prime: "",
        encryptMode: false,
        chats: [],
    };
</script>

<div class="w-full min-h-[100vh] bg-gray-900 pt-10">
    <main
        class=" text-white grid place-items-center grid-cols-3 gap-8 container mx-auto"
    >
        <div class="p-4">
            <Phone owner="User 1" bind:phone otherOwner="User 2" />
        </div>
        <div>
            <div
                class="flex justify-center"
                class:opacity-50={phone.encryptMode}
            >
                <img src="/key.png" class="w-10" alt="" />
            </div>
            <div
                class="flex justify-center mt-4 transition-all"
                class:opacity-50={phone.encryptMode}
            >
                <button
                    on:click={() => {
                        phone.encryptMode = !phone.encryptMode;
                    }}
                    class="bg-gray-800 rounded-tl-md rounded-bl-md p-1 px-2 grid items-center"
                >
                    <img
                        src="/key_black.png"
                        class="aspect-square w-6 invert opacity-60"
                        alt=""
                    />
                </button>
                <input
                    bind:value={phone.key}
                    maxlength="16"
                    type="text"
                    class="w-48 bg-gray-700 rounded-tr-md rounded-br-md px-4 py-2 focus:outline-none text-xl text-gray-300"
                />
            </div>
            <div class="flex justify-center mt-4">
                <button
                    on:click={() => {
                        phone.encryptMode = !phone.encryptMode;
                    }}
                    class="bg-gray-700 px-4 py-1 rounded-md"
                    class:opacity-50={phone.encryptMode}
                >
                    {#if phone.encryptMode}
                        Key Off
                    {:else}
                        Key On
                    {/if}
                </button>
            </div>
            <div class="flex justify-center mt-4 text-gray-300">
                <p>Click to show encrypted/decrypted versions</p>
            </div>
        </div>
        <div class="p-4">
            <Phone owner="User 2" bind:phone otherOwner="User 1" />
        </div>
    </main>
</div>
