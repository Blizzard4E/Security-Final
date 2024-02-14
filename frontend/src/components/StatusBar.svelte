<script>
    import { onMount } from "svelte";
    let time = new Date();
    let batteryPercent = 100;
    let isCharging = false;
    let isOnline = true;
    // these automatically update when `time`
    // changes, because of the `$:` prefix
    $: hours = hours12(time);
    $: minutes = time.getMinutes();

    function hours12(date) {
        return (date.getHours() + 24) % 12 || 12;
    }

    onMount(() => {
        if (navigator.onLine) {
            isOnline = true;
        } else {
            isOnline = false;
        }
        window.addEventListener("offline", (e) => {
            isOnline = false;
        });

        window.addEventListener("online", (e) => {
            isOnline = true;
        });
        navigator.getBattery().then(function (battery) {
            battery.addEventListener("levelchange", function () {
                // Do stuff when the level changes, you can get it
                // from battery.level
                batteryPercent = battery.level * 100;
            });
            batteryPercent = battery.level * 100;
        });
        navigator.getBattery().then((battery) => {
            isCharging = battery.charging;

            battery.addEventListener("chargingchange", () => {
                isCharging = battery.charging;
            });
        });
        const interval = setInterval(() => {
            time = new Date();
        }, 60000);

        return () => {
            clearInterval(interval);
        };
    });
</script>

<div class="py-2 px-5 flex justify-between items-center">
    <h1 class="px-2 text-lg">
        {hours}:{#if minutes < 10}
            0{minutes}
        {:else}
            {minutes}
        {/if}
    </h1>

    <div class="flex gap-2 items-center">
        <img
            src="./wifi.png"
            class="w-[20px] h-auto invert pointer-events-none"
            alt=""
        />
        <div
            class="relative w-8 h-4 rounded-[4px] text-gray-800 grid place-items-center"
        >
            <div
                class="absolute top-0 left-0 bg-gray-100/55 h-full w-full rounded-[3px]"
            ></div>
            <div
                class="absolute top-0 left-0 bg-white h-full rounded-[3px]"
                style={"width: " + batteryPercent + "%"}
                class:bg-white={!isCharging}
                class:bg-green-500={isCharging}
            ></div>
            <div class="mt-[-4px] z-10" class:text-white={isCharging}>
                {Math.round(batteryPercent)}
            </div>
        </div>
    </div>
</div>
