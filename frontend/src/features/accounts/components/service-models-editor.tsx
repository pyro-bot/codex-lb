import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export function ServiceModelsEditor({
  models,
  busy,
  readOnly,
  onSave,
}: {
  models: string[];
  busy: boolean;
  readOnly: boolean;
  onSave: (models: string[]) => Promise<unknown>;
}) {
  const { t } = useTranslation();
  const [draft, setDraft] = useState(models.join(", "));
  useEffect(() => setDraft(models.join(", ")), [models]);
  const save = async () => {
    const next = Array.from(new Set(draft.split(",").map((model) => model.trim()).filter(Boolean)));
    await onSave(next);
  };
  return (
    <div className="rounded-xl border bg-card p-4">
      <p className="text-sm font-medium">{t("accounts.serviceModels.title")}</p>
      <p className="mt-1 text-xs text-muted-foreground">{t("accounts.serviceModels.description")}</p>
      <div className="mt-3 flex gap-2">
        <Input
          aria-label={t("accounts.serviceModels.inputLabel")}
          value={draft}
          disabled={busy || readOnly}
          onChange={(event) => setDraft(event.target.value)}
        />
        <Button type="button" variant="outline" disabled={busy || readOnly} onClick={() => void save()}>
          {t("accounts.serviceModels.save")}
        </Button>
      </div>
    </div>
  );
}
