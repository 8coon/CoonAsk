var ac_editable_toggled = false


function ac_get_attr(el, key) {
    val = el.attr(key)

    if (val == undefined) {
        val = ""
    }

    return val
}


function ac_get_prop(el, key) {
    return el.prop(key)
}


function ac_trim_errors(objects) {

    objects.each(function(i, el) {
        if ($(el).empty()) {
            $(el).hide()
        }
    })

}


function ac_toggle_editable_off() {
    ac_editable_toggled = false

    $("#ac-profile-form-editable .ac-form-editable").each(function(i, el) {
        el = $(el)

        div  = '<div class="ac-former-editable" '
        div += 'ac-former-maxlength="' + ac_get_attr(el, "maxlength") + '" '
        div += 'ac-former-type="' + ac_get_attr(el, "type") + '" '
        div += 'ac-former-class="' + ac_get_attr(el, "class") + '" '
        div += 'ac-former-name="' + ac_get_attr(el, "name") + '" '
        div += 'ac-former-id="' + ac_get_attr(el, "id") + '" '
        div += 'ac-former-placeholder="' + ac_get_attr(el, "placeholder") + '" '
        div += 'ac-former-value="' + ac_get_attr(el, "value") + '" '
        div += 'ac-former-required="' + ac_get_prop(el, "required") + '" '
        div += 'ac-former-tag="' + el.prop("tagName") + '" '
        div += '>' + el.val() + '</div>'

        $(el).replaceWith(div)
    })

}


function ac_toggle_editable_on() {
    ac_editable_toggled = true

    $("#ac-profile-form-editable .ac-former-editable").each(function(i, el) {
        el = $(el)

        input = '<' + ac_get_attr(el, "ac-former-tag") + ' '
        input += 'maxlength="' + ac_get_attr(el, "ac-former-maxlength") + '" '
        input += 'type="' + ac_get_attr(el, "ac-former-type") + '" '
        input += 'class="' + ac_get_attr(el, "ac-former-class") + '" '
        input += 'name="' + ac_get_attr(el, "ac-former-name") + '" '
        input += 'id="' + ac_get_attr(el, "ac-former-id") + '" '
        input += 'placeholder="' + ac_get_attr(el, "ac-former-placeholder") + '" '

        if (ac_get_attr(el, "ac-former-required") == "true") {
            input += 'required'
        }

        if (ac_get_attr(el, "ac-former-tag") == "INPUT") {
            input += 'value="' + ac_get_attr(el, "ac-former-value") + '" '
            input += '>'
        } else {
            input += '>' + el.html()
            input += '</' + ac_get_attr(el, "ac-former-tag") + '>'
        }

        $(el).replaceWith(input)
    })

}


function ac_tinymce_init()
{
    tinymce.init({
        selector: ".ac-textarea-formatted",
        plugins: "link, codesample",
        height: 400,

        allow_conditional_comments: false,
        allow_html_in_named_anchor: false,
        keep_styles: false,
        elementpath: false,
        menubar: false,
        resize: true,
        target_list: false,
        link_title: false,

        toolbar: "undo redo | bold italic underline strikethrough | link blockquote codesample",
        extended_valid_elements: "a[href|target:_blank]",

        /*codesample_languages: [
            {text: 'HTML/XML', value: 'markup'},
            {text: 'JavaScript', value: 'javascript'},
            {text: 'CSS', value: 'css'},
            {text: 'PHP', value: 'php'},
            {text: 'Ruby', value: 'ruby'},
            {text: 'Python', value: 'python'},
            {text: 'Java', value: 'java'},
            {text: 'C', value: 'c'},
            {text: 'C#', value: 'csharp'},
            {text: 'C++', value: 'cpp'},
            {text: 'Lua', value: 'lua'},
        ],*/
    });

    Prism.highlightAll()
}


function ac_toggle_editable(save) {
    if (ac_editable_toggled) {
        if (save) {
            $("#ac-profile-form-editable").submit()
        } else {
            ac_toggle_editable_off()

            $("#ac-profile-edit").text("Edit")
            $("#ac-profile-discard").hide()
        }
    } else {
        ac_toggle_editable_on()
        $("#ac-profile-edit").text("Save")
        $("#ac-profile-discard").show()

        ac_tinymce_init()
    }

    ac_trim_errors($(".ac-field-error-text-container"))
}


$(document).ready(function() {

    $(".ac-avatar-preview").click(function() {
        document.location.href = $(this).attr("ac-href")
    })

    $("#ac-profile-edit").click(function() {
        ac_toggle_editable(true)
    })

    $("#ac-profile-discard").click(function() {
        ac_toggle_editable(false)
    })

    ac_toggle_editable_off()
    ac_trim_errors($(".ac-field-error-text-container"))
    ac_tinymce_init()

    $("#ac-profile-discard").hide()
})