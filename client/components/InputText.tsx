import axios from "axios";
import * as React from "react";
import { ChangeEvent, useCallback, useState } from "react";
import { Alert, Button, FormGroup, Input, Label } from "reactstrap";
import { apiUrl } from "../util/misc";
import { None, Option, Some } from "../util/option";

interface Props {
    onSave: (id: number) => void;
}

const InputText = (props: Props) => {
    const [value, setValue] = useState<Option<string>>(None);
    const [error, setError] = useState<Option<string>>(None);
    const [loading, setLoading] = useState(false);

    const onChange = useCallback((evt: ChangeEvent<HTMLInputElement>) => {
        setValue(Some(evt.target.value));
    }, [value]);

    const onClick = useCallback(async () => {
        setLoading(true);
        const res = await axios
          .post<{ id: number }>(
            apiUrl("/snippet"),
            value,
          )
          .then(r => r.data)
          .catch(e => setError(e.message));
        if(res) {
            props.onSave(res.id);
        }
        setLoading(false);
    }, [value, props.onSave]);

    const onDismiss = () => {
        setError(None);
    };

    const alert = error.map(e =>
      <Alert color="danger" isOpen={true} toggle={onDismiss}>{e}</Alert>,
    ).getOrElse(
      <Label className="mt-3 mb-4 p-0" for="exampleText">
          Paste text here to save for content analysis
      </Label>,
    );
    return (
      <>
          {alert}
          <FormGroup>
              <Input
                disabled={loading}
                rows={10}
                type="textarea"
                name="text"
                id="textToParse"
                bsSize="lg"
                onChange={onChange}
                value={value.getOrElse("")}
              />
              <Button
                disabled={loading}
                className="btn btn-lg mt-2 float-right"
                onClick={onClick}
              >Save</Button>
          </FormGroup>
      </>
    );
};

export default InputText;
