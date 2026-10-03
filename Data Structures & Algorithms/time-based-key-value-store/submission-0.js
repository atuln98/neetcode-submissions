class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
       if (!this.keyStore.has(key)) {
            this.keyStore.set(key, []);
        }
        this.keyStore.get(key).push([timestamp, value]);
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
       const list = this.keyStore.get(key);
        if (!list) return "";

        let l = 0, r = list.length - 1;
        let res = "";

        while (l <= r) {
            const m = Math.floor((l + r) / 2);
            if (list[m][0] <= timestamp) {
                res = list[m][1];   // valid candidate, look right for a later one
                l = m + 1;
            } else {
                r = m - 1;          // too new, look left
            }
        }
        return res;
    }
}
