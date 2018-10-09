const St = imports.gi.St;
const Main = imports.ui.main;
const Soup = imports.gi.Soup;
const Lang = imports.lang;
const Mainloop = imports.mainloop;
const Clutter = imports.gi.Clutter;
const PanelMenu = imports.ui.panelMenu;


var date = new Date();
var year = date.getFullYear().toString()
var month = (date.getMonth()+1).toString();
var TW_URL = 'http://qtracker.qburst.com/v2/api/attendance-tracker/user/monthly-status?month='+month+'&year='+year;
var TW_AUTH_KEY = '';

// global.log('day = ' + day)
// global.log('month = '+month)
// global.log('year = '+ year)

let _httpSession;
const TransferWiseIndicator = new Lang.Class({
  Name: 'TransferWiseIndicator',
  Extends: PanelMenu.Button,

  _init: function () {
    this.parent(0.0, "Transfer Wise Indicator", false);
    this.buttonText = new St.Label({
      text: _("Loading..."),
      y_align: Clutter.ActorAlign.CENTER
    });
    this.actor.add_actor(this.buttonText);
    this._refresh();
  },

  _refresh: function () {
    this._loadData(this._refreshUI);
    this._removeTimeout();
    this._timeout = Mainloop.timeout_add_seconds(100, Lang.bind(this, this._refresh));
    return true;
  },

  _loadData: function () {
    _httpSession = new Soup.Session();
    let message = Soup.Message.new('GET', TW_URL);
    message.request_headers.append("Authorization", TW_AUTH_KEY);
    _httpSession.queue_message(message, Lang.bind(this, function (_httpSession, message) {
          if (message.status_code !== 200)
            return;
          let json = JSON.parse(message.response_body.data);
          this._refreshUI(json);
        }
      )
    );
  },

  _refreshUI: function (data) {
    var i =(new Date()).getDate()-1;
    var clocked_hour = parseInt(data.payload.monthlyData[i].hours_clocked,10 ).toString();
    var clocked_minute = formatInt((data.payload.monthlyData[i].hours_clocked*60)%60).toString().substring(0,2);

    var burned_hour = parseInt(data.payload.monthlyData[i].hours_burned.toString(),10);
    var burned_minute = formatInt((data.payload.monthlyData[i].hours_burned*60)%60).toString().substring(0,2);
    // let txt = data.payload.monthlyData[7].hours_clocked.toString() + " : " + data.payload.monthlyData[7].hours_burned.toString();
    let txt = clocked_hour + ":" + clocked_minute + " -> " + burned_hour + ":" + burned_minute;
    // global.log(txt);
    this.buttonText.set_text(txt);
  },

  _removeTimeout: function () {
    if (this._timeout) {
      Mainloop.source_remove(this._timeout);
      this._timeout = null;
    }
  },

  stop: function () {
    if (_httpSession !== undefined) 
      _httpSession.abort();
    _httpSession = undefined;

    if (this._timeout)
      Mainloop.source_remove(this._timeout);
    this._timeout = undefined;

    this.menu.removeAll();
  }
});

let twMenu;

function init() {
}

function enable() {
  twMenu = new TransferWiseIndicator;
  Main.panel.addToStatusArea('tw-indicator', twMenu);
}

function disable() {
  twMenu.stop();
  twMenu.destroy();
}

function formatInt(n){
  return n > 9 ? "" + n: "0" + n;
}
