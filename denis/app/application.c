#include <application.h>

// LED instance
bc_led_t led;

int p = 0, q=0;

//Funciton which is getting data from dongl
void get_data(uint64_t *id, const char *topic, void *value, void *param);

// LEDs
bc_led_t red;
bc_led_t yellow;
bc_led_t green;

//Taska
bc_scheduler_task_id_t red_task;
bc_scheduler_task_id_t yellow_task_on;
bc_scheduler_task_id_t yellow_task_off;
bc_scheduler_task_id_t green_task;

// Button instance
bc_button_t button;

static const bc_radio_sub_t data[] = {
        {"alarm/-/set/state", BC_RADIO_SUB_PT_INT, get_data, NULL}
};

void get_data(uint64_t *id, const char *topic, void *value, void *param) {

        bc_log_debug("data: " + *(int*)value);

        if(*(int*)value == 0 && q == 0) //stoj
        {

            bc_scheduler_plan_from_now(red_task, 2500);
            bc_led_set_mode(&yellow, BC_LED_MODE_TOGGLE);
            bc_scheduler_plan_from_now(yellow_task_off, 2500);
            bc_scheduler_plan_from_now(green_task, 2500);
            q=1;
        }
        else if(*(int*)value == 1 && q == 1){ //jed

            bc_led_set_mode(&green, BC_LED_MODE_TOGGLE);
            bc_led_set_mode(&yellow, BC_LED_MODE_TOGGLE);
            bc_scheduler_plan_from_now(yellow_task_off, 2500);
            bc_scheduler_plan_from_now(red_task, 2500);
            q=0;
        } 
}

static void red_blink() {
    bc_led_set_mode(&red, BC_LED_MODE_TOGGLE);
}

static void yellow_on() {
    bc_led_set_mode(&yellow, BC_LED_MODE_TOGGLE);
}

static void yellow_off() {
    bc_led_set_mode(&yellow, BC_LED_MODE_TOGGLE);
}

static void green_blink() {
    bc_led_set_mode(&green, BC_LED_MODE_TOGGLE);
}


void button_event_handler(bc_button_t *self, bc_button_event_t event, void *event_param)
{

    if (event == BC_BUTTON_EVENT_PRESS)
    {
        if(p == 0) //stoj
        {

            bc_log_debug("stoj");
            bc_scheduler_plan_from_now(red_task, 2500);
            bc_led_set_mode(&yellow, BC_LED_MODE_TOGGLE);
            bc_scheduler_plan_from_now(yellow_task_off, 2500);
            bc_scheduler_plan_from_now(green_task, 2500);

            p=1;
        }
        else if(p == 1){ //jed

            bc_log_debug("jed");
            bc_led_set_mode(&green, BC_LED_MODE_TOGGLE);
            bc_led_set_mode(&yellow, BC_LED_MODE_TOGGLE);
            bc_scheduler_plan_from_now(yellow_task_off, 2500);
            bc_scheduler_plan_from_now(red_task, 2500);

            p=0;
        }
    }

    // Logging in action
    bc_log_info("Button event handler - event: %i", event);
}

void application_init(void)
{
    // Initialize logging
    bc_log_init(BC_LOG_LEVEL_DUMP, BC_LOG_TIMESTAMP_ABS);

    bc_radio_init(BC_RADIO_MODE_NODE_LISTENING);

    bc_radio_pairing_request("semafor2", VERSION);

    bc_radio_set_subs((bc_radio_sub_t *) data, sizeof(data) / sizeof(bc_radio_sub_t));

    // Initialize LED
    bc_led_init(&red, BC_GPIO_P0, false, false);
    bc_led_init(&yellow, BC_GPIO_P1, false, false);
    bc_led_init(&green, BC_GPIO_P2, false, false);

    // Initialize button
    bc_button_init(&button, BC_GPIO_BUTTON, BC_GPIO_PULL_DOWN, false);
    bc_button_set_event_handler(&button, button_event_handler, NULL);

    // Initialize traffic light to green

    bc_led_set_mode(&red, BC_LED_MODE_ON);

    // Initialize tasks

    red_task = bc_scheduler_register(red_blink, NULL, BC_TICK_INFINITY);
    yellow_task_on = bc_scheduler_register(yellow_on, NULL, BC_TICK_INFINITY);
    yellow_task_off = bc_scheduler_register(yellow_off, NULL, BC_TICK_INFINITY);
    green_task = bc_scheduler_register(green_blink, NULL, BC_TICK_INFINITY);

}